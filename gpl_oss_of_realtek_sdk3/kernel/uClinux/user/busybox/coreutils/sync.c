/* vi: set sw=4 ts=4: */
/*
 * Mini sync implementation for busybox
 *
 * Copyright (C) 1995, 1996 by Bruce Perens <bruce@pixar.com>.
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
 *
 */

/* BB_AUDIT SUSv3 N/A -- Matches GNU behavior. */

#include <stdlib.h>
#include <unistd.h>
#ifdef EMBED
#include <config/autoconf.h>
#include <signal.h>
#endif
#include "busybox.h"

extern int sync_main(int argc, char **argv)
{
#ifdef CONFIG_USER_FLATFSD_FLATFSD
	int   verbose = 0;
	int   flash = 0;
	int   opt;

	while ((opt=getopt(argc, argv, "vf")) != -1) {
		switch(opt) {
			case 'v':
				verbose = 1;
				break;
			case 'f':
				flash = 1;
				break;
			default:
				bb_show_usage();
		}
	}

	/* get the pid of flatfsd */
	if (flash) {
		if (verbose)
			puts("sync: flash");
		system("exec flatfsd -s");
	}
	if (verbose)
		puts("sync: file systems");
#else
	bb_warn_ignoring_args(argc - 1);
#endif

	sync();

	return(EXIT_SUCCESS);
}
