#this file uses modified and unmodified code from the talon voice community repository
#located here: https://github.com/knausj85/knausj_talon
#under the following license:
#MIT License
#
#Copyright (c) 2021 Jeff Knaus, Ryan Hileman, Zach Dwiel, Michael Arntzenius, and others
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
#
#(end of the community repository license)


not tag: user.line_commands
and tag: /(code|^(user.protobuf|user.go|user.markdown|user.batch)$)/i
header requires that the regular knausj line commands are not enabled
#and a tag with the word code in it (case insensitive) or one of the
#tags for languages that knausj currently supports at the time that this
#comment was written that do not use any tags with the word code in it
#using force <language name> with knausj should enable these commands
#without the user.line_commands tag for most knausj supported languages
-
#these two commands were taken from the community repository without modification
lend: edit.line_end()
bend: edit.line_start()

go <number> :
    user.unsupported_go_to_line(number)
go <number> end:
    user.unsupported_go_to_line(number)
    edit.line_end()

comment [line] <number>:
    user.unsupported_go_to_line(number)
    user.unsupported_comment_current_line()


clear [line] <number>:
    user.unsupported_go_to_line(number)
    edit.select_line()
    edit.delete()
clear <number> until <number>:
    user.unsupported_select_lines(number_1, number_2)
    edit.delete()

(select|cell|sell) <number>:
    user.unsupported_go_to_line(number)
    edit.select_line()
(select|cell|sell) <number> until <number>:
    user.unsupported_select_lines(number_1, number_2)

copy [line] <number>:
    user.unsupported_go_to_line(number)
    edit.select_line()
    edit.copy()
copy <number> until <number>:
    user.unsupported_select_lines(number_1, number_2)
    edit.copy()

cut [line] <number>:
    user.unsupported_go_to_line(number)
    edit.select_line()
    edit.cut()
cut <number> until <number>:
    user.unsupported_select_lines(number_1, number_2)
    edit.cut()

(paste|replace) <number> until <number>:
    user.unsupported_select_lines(number_1, number_2)
    edit.paste()

tab that: 
    user.unsupported_indent_line()
tab [line] <number>:
    user.unsupported_go_to_line(number)
    key(tab)
tab <number> until <number>:
    user.unsupported_indent_lines_in_range(number_1, number_2)
retab that:
    user.unsupported_select_entire_line()
    edit.left()
    edit.extend_right()
    edit.delete()
retab [line] <number>: 
    user.unsupported_go_to_line(number)
    user.unsupported_reduce_indentation_from_line_start()
retab <number> until <number> [<user.ordinals>]:
    user.unsupported_deindent_lines_in_range(number_1, number_2, ordinals or 1)


drag [line] down:
    user.unsupported_drag_line_down()
drag [line] up:
    user.unsupported_drag_line_up()


clone (line|that):
    user.unsupported_clone_line()
    


