# todo: Pythonista のショートカット機能を使ってね📲

import scene, editor, pathlib, ui

src = editor.get_text()
img = None  #scene.Texture('_UVCheckerMap01-512.png')


class MyScene(scene.Scene):
  def setup(self):
    node = scene.Node(self.size / 2)
    self.add_child(node)
    sp_node = scene.ShapeNode(parent=node)
    x_line = scene.ShapeNode(parent=node)
    x_path = ui.Path()
    x_path.move_to(0.0, self.size.y)
    x_path.line_to(self.size.x, self.size.y)
    x_line.path = x_path
    x_line.stroke_color = 'maroon'

    y_line = scene.ShapeNode(parent=node)
    y_path = ui.Path()
    y_path.move_to(self.size.x, 0.0)
    y_path.line_to(self.size.x, self.size.y)
    y_line.path = y_path
    y_line.stroke_color = 'maroon'

    self.shdr = scene.SpriteNode(parent=self)
    #self.shdr.texture = img
    _x = self.size.x * .88
    self.shdr.size = (_x, _x)
    #shdr.size=self.size
    self.shdr.shader = scene.Shader(src)
    self.shdr.shader.set_uniform('u_resolution', (_x, _x))
    # todo: Initial position before touching
    self.shdr.shader.set_uniform('u_offset', (0.5, 0.5))

    sp_node.size = self.shdr.size
    sp_node.color = 'darkslategray'
    #sp_node.color = 'skyblue'
    self.did_change_size()

  def did_change_size(self):
    # todo: Center the image
    self.shdr.position = self.size / 2

  def touch_began(self, touch):
    self.set_uniform_touch(touch)

  def touch_moved(self, touch):
    self.set_uniform_touch(touch)

  def set_uniform_touch(self, touch):
    if touch.location in self.shdr.frame:
      local_touch = touch.location - self.shdr.frame
      dx = local_touch[0] / self.shdr.size[0]
      dy = local_touch[1] / self.shdr.size[1]
      self.shdr.shader.set_uniform('u_offset', (dx, dy))


main = MyScene()
scene.run(main, show_fps=True, frame_interval=0)

