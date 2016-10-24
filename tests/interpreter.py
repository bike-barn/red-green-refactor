import pytest

import pascal_interpreter as p_interp


def test_interpreter_blank_program():
    input_text = ""
    interp = p_interp.Interpreter(text=input_text)
    # If this doesn't barf we're good.


def test_interpreter_error_type():
    input_text = ""
    interpreter = p_interp.Interpreter(text=input_text)
    with pytest.raises(p_interp.InterpreterError):
        interpreter._error()


def test_invalid_string_errors():
    input_text = "This is currently an error"
    interpreter = p_interp.Interpreter(text=input_text)
    with pytest.raises(p_interp.InterpreterError):
        interpreter._next_token()


def test_eof_token_at_end_of_line():
    input_text = ""
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter._next_token().type == p_interp.EOF


def test_eof_token_after_int():
    input_text = "1"
    interpreter = p_interp.Interpreter(text=input_text)
    token = interpreter._next_token()
    assert token.type == p_interp.INTEGER
    assert token.value == 1
    assert interpreter._next_token().type == p_interp.EOF


def test_consume_valid_token():
    input_text = "1+1"
    interpreter = p_interp.Interpreter(text=input_text)
    # Mistake: Since _next_token changes the state of position you can't just
    # interpreter.current_token = p_interp.Token(p_interp.INTEGER, 1)
    # You have to call _next_token.
    interpreter.current_token = interpreter._next_token()
    interpreter._consume_token(p_interp.INTEGER)
    assert interpreter.current_token.type == p_interp.PLUS


def test_consume_invalid_token():
    input_text = "+1"
    interpreter = p_interp.Interpreter(text=input_text)
    interpreter.current_token = interpreter._next_token()
    with pytest.raises(p_interp.InterpreterError):
        interpreter._consume_token(p_interp.INTEGER)

def test_parse_addition():
    # NOTE: I misnamed this test function. Another function had the same name
    # For a little while and as such this test was never ran.
    input_text = "1+1"
    interpreter = p_interp.Interpreter(text=input_text)
    assert interpreter.parse() == 2

def test_parse_sets_eof():
    input_text = "1+1"
    interpreter = p_interp.Interpreter(text=input_text)
    interpreter.parse()
    assert interpreter.current_token.type == p_interp.EOF


def test_parse_invalid_addition():
    input_text = "+1"
    interpreter = p_interp.Interpreter(text=input_text)
    with pytest.raises(p_interp.InterpreterError):
        interpreter.parse()
