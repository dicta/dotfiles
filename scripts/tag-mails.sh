#!/bin/sh

# Don't mark as inbox anything that's not to me directly.
notmuch tag -inbox -unread not to:dan@structuredgrid.net

# Mailing lists
notmuch tag  +uboot      to:u-boot@lists.denx.de 
notmuch tag  +kernel-arm to:linux-arm-kernel@lists.infradead.org
notmuch tag  +lkml       to:linux-kernel@vger.kernel.org