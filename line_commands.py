from talon import Module, actions, clip


mod = Module()

line_limit = mod.setting(
    'unsupported_application_programming_line_limit',
    type = int,
    default = 1000,
    desc = 'The limit of how far the line jumping feature is willing to jump. Prevents the commands from accidentally taking an extremely long time due to accidentally dictating a gigantic number'
)

clipboard_operation_delay = mod.setting(
    'unsupported_application_programming_clipboard_operation_delay',
    type = int,
    default = 200,
    desc = 'How long the unsupported application programming commands should pause when doing copying and pasting while preserving the clipboard'
)



@mod.action_class
class Actions:
    def unsupported_go_to_line(line_number: int):
        '''Goes to the specified line in most unsupported applications'''
        if line_number_below_limit(line_number): 
            actions.edit.file_start()
            if line_number > 1:
                for iteration in range(0, line_number - 1):
                    actions.edit.down()
    def unsupported_select_lines(starting_line_number: int, final_line_number: int):
        '''Selects the specified lines in most unsupported applications'''
        if not valid_line_range(starting_line_number, final_line_number):
            return 
        actions.user.unsupported_go_to_line(starting_line_number)
        for iteration in range(starting_line_number, final_line_number + 1):
            actions.edit.extend_down()
    def unsupported_select_entire_line():
        '''Selects the entire line in most unsupported applications'''
        actions.edit.line_end()
        actions.edit.extend_line_start()
        actions.edit.extend_line_start()

    def unsupported_indent_line():
        '''Indents the current line'''
        indent_line()
    def unsupported_indent_lines_in_range(start: int, final: int):
        '''Indents the specified lines in most applications'''
        perform_action_at_each_line(start, final, indent_line)
    def unsupported_reduce_indentation_from_line_start():
        '''Reduces the indentation assuming that the cursors at the line's start in most applications'''
        actions.edit.extend_right()
        actions.edit.delete() 
    def unsupported_deindent_lines_in_range(start: int, final: int, times: int):
        '''Reduces the indentation of the specified lines in most applications'''
        def less_indentation_action():
            for iteration in range(times):
                actions.user.unsupported_reduce_indentation_from_line_start()
        perform_action_at_each_line(start, final, less_indentation_action)
    
    def unsupported_comment_current_line():
        '''Comments the current line in most applications'''
        actions.user.unsupported_select_entire_line()
        actions.edit.left()
        actions.user.code_comment_line_prefix()


    def unsupported_clone_line():
        '''Clones the current line in most applications'''
        line_text = get_line()
        actions.edit.right()
        actions.key('enter')
        paste_text(line_text)
    def unsupported_drag_line_down():
        '''Drags the line down one line in most unsupported applications'''
        text = cut_line()
        actions.edit.delete()
        actions.edit.down()
        start_line_below()
        paste_text(text)
    def unsupported_drag_line_up():
        '''Drags the line up one line in most applications'''
        bottom_text = cut_line()
        actions.edit.delete()    
        actions.edit.line_start()
        top_text = cut_line()
        paste_text(bottom_text)
        actions.key('enter')
        actions.user.unsupported_select_entire_line()
        paste_text(top_text)

    

def line_number_below_limit(number):
    return number <= line_limit.get()

def start_line_below():
    actions.edit.line_end()
    actions.key('enter')

def perform_action_at_each_line(starting_line_number, final_line_number, action):
    if valid_line_range(starting_line_number, final_line_number):
        actions.user.unsupported_go_to_line(starting_line_number)
        for iteration in range(starting_line_number, final_line_number + 1):
            action()
            actions.edit.down()

def valid_line_range(start, final):
    return  line_number_below_limit(start) and line_number_below_limit(final) and start <= final

def paste_text (text: str):
    with clip.revert():
        clip.set_text(text)
        actions.edit.paste()
        wait_long_enough_to_let_clipboard_revert_properly()
def cut_line():
    text = get_line()
    actions.edit.delete()
    return text

def get_line():
    '''Returns the current line'''
    with clip.revert():
        actions.user.unsupported_select_entire_line()
        actions.edit.copy()
        wait_long_enough_to_let_clipboard_revert_properly()
        result = clip.text()
    return result

def wait_long_enough_to_let_clipboard_revert_properly():
    actions.sleep(f'{clipboard_operation_delay.get()}ms')

def indent_line():
    actions.edit.line_start()
    actions.key('tab')
