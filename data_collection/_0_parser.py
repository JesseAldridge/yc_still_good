
class Parser:
  def __init__(self, text):
    self.lines = text.splitlines()
    self.line_index = 0

  def line(self):
    return self.lines[self.line_index]

  def apply_cmd(self, cmd_str, params):
    getattr(self, cmd_str)(*params)

  def next_line(self):
    self.line_index += 1
    return self.line()

  def stop_after(self, stop_line):
    for _ in range(10 ** 6):
      if self.lines[self.line_index].strip() == stop_line:
        break
      self.line_index += 1
    self.line_index += 1

  def is_done(self):
    return self.line_index >= len(self.lines)

  def status_str(self):
    return 'line {}/{}'.format(self.line_index, len(self.lines))

if __name__ == '__main__':
  def test():
    parser = Parser('foo\nbar\nbaz\nother thing\nok ok\n')

    def check(expected):
      print(parser.line())
      assert parser.line() == expected

    check('foo')
    parser.apply_cmd('next_line', [])
    check('bar')
    parser.apply_cmd('stop_after', ['other thing'])
    check('ok ok')
  test()
