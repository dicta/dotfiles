#!/usr/bin/env python

import sys
import optparse
import mailbox
import email.Errors
from pyparsing import alphanums, Word, SkipTo, ParseException, Or

### Options

# all converted mail will be stored here.
mail_store = "~/@MAILBOX/Imported"

### End options

def main():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--infile', dest='infile', default=None,
                  help='input mailbox file', metavar='MAILBOX')
    parser.add_option('-p', '--pipermail', action="store_true", dest="pipermail", default=False,
                  help='whether to de-obfuscate pipermail-exported From addresses')
    options, args = parser.parse_args()

    if not options.infile:
        parser.print_help()
        sys.exit(1)

    inbox  = mailbox.mbox(options.infile)
    outbox = mailbox.Maildir(mail_store, factory=None)

    import_mail(src=inbox, dest=outbox, fix_pipermail=options.pipermail)

    outbox.close()
    inbox.close()
    print "Conversion complete."

def import_mail(src, dest, fix_pipermail=False):
    count = 0
    for key in src.iterkeys():
        try:
            message = src[key]
        except email.Errors.MessageParseError:
            print "Parse Error", str(key)
            continue # The message is malformed. Just leave it.
        
        if "From" not in message.keys():
            print "Malformed data: no 'From' header in email."
            print message.items()
            continue

        if fix_pipermail:
            # For pipermail imports... notmuch doesn't like nonconforming/obfuscated From lines.
            message.replace_header("From", convert_mangled_from(message["From"]))
            
            dest.add(message)
            
            count = count + 1
            if count % 200 == 0:
                print "- %d messages" % count

    # Finish up.
    print "- %d messages total." % count


# Build a little parser to convert the mangled e-mail addresses output by pipermail.
# input: "user at domain.com (Real Name)"
email_alphas = alphanums + "_-+."

email_addr = Word(email_alphas).setResultsName("email_name") + "at" + Word(email_alphas).setResultsName("email_domain")

from_line = Or(email_addr + "(" + SkipTo(")").setResultsName("name") + ")",
               SkipTo("<").setResultsName("name") + "<" + email_addr + ">")

def convert_mangled_from(input_string):
    """Converts pipermail export-mangled e-mail addresses.
       input_string: 'user at domain (Real Name)'
       returns standard format: '"Real Name" <user@domain>"""
    try:
        parse_result = from_line.parseString(input_string)
        return '"%s" <%s@%s>' % (parse_result.name, parse_result.email_name, parse_result.email_domain) 
    except ParseException, e:
        print "Could not parse mangled e-mail address: %s" % input_string
        print str(e)
        return input_string
    except AttributeError:
        print "Malformed input: %s" % input_string
        return input_string

if __name__ == "__main__":
    main()
