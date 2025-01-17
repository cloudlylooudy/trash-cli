# Copyright (C) 2011-2021 Andrea Francia Bereguardo(PV) Italy
import os
import sys

from trashcli.fs import FsMethods
from trashcli.fstab.volume_listing import RealVolumesListing
from trashcli.rm.rm_cmd import RmCmd, RmFileSystemReader


def main():
    volumes_listing = RealVolumesListing()
    cmd = RmCmd(environ=os.environ,
                getuid=os.getuid,
                volumes_listing=volumes_listing,
                stderr=sys.stderr,
                file_reader=RealRmFileSystemReader())

    cmd.run(sys.argv, os.getuid())

    return cmd.exit_code


class RealRmFileSystemReader(RmFileSystemReader):
    is_sticky_dir = FsMethods().is_sticky_dir
    is_symlink = FsMethods().is_symlink
    contents_of = FsMethods().contents_of
    entries_if_dir_exists = FsMethods().entries_if_dir_exists
    exists = FsMethods().exists
