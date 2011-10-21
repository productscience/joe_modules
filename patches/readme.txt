To create a diff,

* Make a backup copy of the original file. sudo cp the_file.py the_file.py.backup
* Edit the original until it works in the new way.
* sudo cp the_file.py the_file.py.changed 
* sudo cp the_file.py.backup the_file.py (I.e. restore the original from the backup. Need orginal to have same name as before and be in old state because this name is stored in the diff as the target for the patch)
* Then choose an appropriate source root directory (e.g the django install directory).
* CD into this.
* sudo diff -c path/to/the_file.py path/to/the_file.py.changed > ~/django_projects/modules/patches/good_name_for_patch.diff
     (probably don't need sudo for this one)
* Then test the diff by staying in the chosen source root directory and:
     sudo patch -N -p0 -i ~/django_projects/modules/patches/good_name_for_patch.diff

To make this happen on the server:
* Edit clients.py and add an entry under env.patches. ['good_name_for_patch.diff', 'equivalent of chosen_root on the server'], ...
* Go to django_projects/modules/patches and do an svn commit
* Then run fab xxxx setup
* Then run fab xxxx update ('cos setup won't restart nginx, it only starts it if not running)
