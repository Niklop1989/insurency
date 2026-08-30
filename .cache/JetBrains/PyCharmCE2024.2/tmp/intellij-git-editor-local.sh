#!/bin/sh
"/snap/pycharm-community/436/jbr/bin/java" -cp "/snap/pycharm-community/436/plugins/vcs-git/lib/git4idea-rt.jar:/snap/pycharm-community/436/lib/externalProcess-rt.jar" git4idea.editor.GitRebaseEditorApp "$@"
