import argparse # module to parse command line 
import configparser # git uses a cinfigruation file format need specific moduel to writ it 
from datetime import datetime # we will do some date and time manipulatoin

import os
import grp, pwd  # read groups and users from git

from fnmatch import fnmatch # to match file names with patterns like git ignore

import hashlib

from math import ceil

import re , sys , zlib

argparser = argparse.ArgumentParser(description="The stupidest content tracker")

# call git and it command (sub parser)
argsubparsers = argparser.add_subparsers(title="Commands", dest="command")
argsubparsers.required = True

def main(argv=sys.argv[1:]):
    args = argparser.parse_args(argv)
    match args.command:
        case "add"          : cmd_add(args)
        case "cat-file"     : cmd_cat_file(args)
        case "check-ignore" : cmd_check_ignore(args)
        case "checkout"     : cmd_checkout(args)
        case "commit"       : cmd_commit(args)
        case "hash-object"  : cmd_hash_object(args)
        case "init"         : cmd_init(args)
        case "log"          : cmd_log(args)
        case "ls-files"     : cmd_ls_files(args)
        case "ls-tree"      : cmd_ls_tree(args)
        case "rev-parse"    : cmd_rev_parse(args)
        case "rm"           : cmd_rm(args)
        case "show-ref"     : cmd_show_ref(args)
        case "status"       : cmd_status(args)
        case "tag"          : cmd_tag(args)
        case _              : print("Bad command.")


class GitRepository (object):
    """A git repository"""

    worktree = None
    gitdir = None
    conf = None
    # dssf
    def __init__(self, path, force=False):
        self.worktree = os.path.join(path, ".git")

        if not (force or os.path.join(self.gitdir)):
            raise Exception(f"Not a Git repo {path}")
        
        self.conf = configparser.ConfigParser()
        cf = repo_file(self, "config")

        if cf and os.path.exists(cf):
            self.conf.read([cf])
        elif not force:
            raise Exception("Configuration file missing")
        
        if not force:
            vers = int(self.conf.get("core", "repositoryformatversion"))
            if vers != 0:
                raise Exception("Unsupported repositoryformatversion: {vers}")
        
    def repo_path(repo, *path):
        """Compute path under repo's gitdir."""
        return os.path.join(repo.gitdir, *path)
    
    def repo_file(repo, *path, mkdir=False):
        """same as repo path, but create dir name  if absent. For example , repo file will create .git 
        refs/remotes/origin"""

        if repo_dir(repo, *path[:-1], mkdir=mkdir):
            return repo_path(repo, *path)

    def repo_dir(repo, *path, mkdir=False):
        """same as repo path, but mkdire if absent """

        path = repo_path(repo, *path)

        if os.path.exists(path):
            if(os.path.isdir(path)):
                return path
            else:
                raise Exception(f"Not a directory {path}")
        
        if mkdir:
            os.makedirs(path)
            return path
        else:
            return None
