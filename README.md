# Talon-Voice-Unsupported-Editor-Programming
The project contains Talon commands for working with editors that do not support programming or you do not have specific configuration for. The code assumes that you have the Talon community repository commands/configuration installed: (https://github.com/knausj85/knausj_talon).

# Line Commands
Please note that the line commands documentation is incomplete.

The line commands require that the community repository tag user.line_commands is not active (to avoid overwriting the community repository line commands when they are available). They also require that a tag with the word code in it is active or one of several community repository programming tags supported by this project. At the time of writing this documentation, one should be able to activate these line commands in an application without the community repository line commands tag by using the community of repository force language command with any of its supported languages.

The following line commands are provided: (text in square brackets is optional)

lend: goes to the end of the line.

bend: goes to the beginning of the line.

go (line number): goes to the specified line number by going to the top and then going down enough times to get to the desired line. This is typically quick for small line numbers but long for large ones. To prevent the user from accidentally using this command with massive numbers and consequently freezing Talon for a while, a setting is provided limiting the maximum line number that the command will go to (1000 by default). All line commands that move to the desired line do it with this process and respecting that limit.

go (line number) end: goes to the end of the specified line.

comment [line] (line number): goes to the specified line and puts the active programming language's line comment symbol assuming that the user.code_commented_line_prefix action is defined appropriately within the active context.

clear [line] (line number): goes to the specified line and removes it.

clear (line number) until (line number): selects from the first line number to the second line number and then deletes the lines assuming that the first line number does not exceed the second and neither line number goes over the limit. All subsequent line commands that deal with a range of lines go from the first line number to the second if the first does not exceed the second and neither exceed the limit.

select (line number): goes to the specified line and selects it.

select (line number) until (line number): selects the lines in the specified range.

cut [line] (line number): goes to the specified line and cuts it.

cut (line number) until (line number): selects the specified lines and cuts them.

(paste|replace) (line number) until (line number): selects the specified lines and then pastes.
  




# Giving Credit
This project contains modified and unmodified code from the community repository mentioned above provided under the following license:
"MIT License

Copyright (c) 2021 Jeff Knaus, Ryan Hileman, Zach Dwiel, Michael Arntzenius, and others

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."
