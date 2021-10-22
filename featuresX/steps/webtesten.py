from behave import *


## write
@given(u'There is an empty text file available to us')
def step_impl(context):
    context.filename = 'empty_file'
    context.f = open(context.filename,'wt') 
    context.f.close
    assert context.filename == 'empty_file'
    # assert context.f.name is context.filename


@when(u'I open this file')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I open this file')

@when(u'I write the following table in it')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I write the following table in it')

@then(u'This file has 3 lines in it')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then this file has 3 lines in it')

# some
@given(u'The text file has been opened')
def step_impl(context):
    raise NotImplementedError(u'STEP: The text file has been opened')

@then(u'I write the values {one}, {two} and {three}')
def step_impl(context, one, two, three):
    raise NotImplementedError(u'STEP: Then I write the values')

@then(u'I close the file')
def step_impl(context, one, two, three):
    raise NotImplementedError(u'STEP: Then I close the file')


def add_line_to_file(filename, this_line):
  f = open(filename, "at")
  f.write(this_line + "\n")
  f.close()