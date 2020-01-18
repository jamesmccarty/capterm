#!/usr/bin/env python

from pymol import editor, cmd

cmd.load('singlechain.pdb')

editor.attach_amino_acid("last name C", 'nme')
editor.attach_amino_acid("first name N", 'ace')

cmd.set('pdb_use_ter_records',0)
cmd.save('cappedchain.pdb')
