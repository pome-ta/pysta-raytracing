import scene, editor, pathlib, ui

src = editor.get_text()
#_img = ui.Image.named('sample.png')
#_img = ui.Image.named('dummy.PNG')
#_img = ui.Image.named('Kanata_1024.png')
#_img = ui.Image.named('unity.png')
#_img = ui.Image.named('pix.PNG')
#img = scene.Texture(_img)
#img = scene.Texture('test:Mandrill')
img = None#scene.Texture('_UVCheckerMap01-512.png')



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



if __name__ == '__main__':
  src = '''
  precision highp float;

uniform float u_time;
uniform vec2 u_sprite_size;
//uniform float u_scale;
uniform sampler2D u_texture;
//uniform vec4 u_tint_color;
//uniform vec4 u_fill_color;
varying vec2 v_tex_coord;


void main(){
  float t = u_time;
  vec2 uv = (v_tex_coord- vec2(0.5)) *2.0;
  
  vec3 cPos = vec3(0.0,  0.0,  3.0); // カメラの位置
  vec3 cDir = vec3(0.0,  0.0, -1.0); // カメラの向き(視線)
  vec3 cUp  = vec3(0.0,  1.0,  0.0); // カメラの上方向
  vec3 cSide = cross(cDir, cUp);     // 外積を使って横方向を算出
  float targetDepth = 0.1;           // フォーカスする深度
    
  // ray
  vec3 ray = normalize(cSide * uv.x + cUp * uv.y + cDir * targetDepth);
    
  
  
  uv = uv / 2.0 + vec2(0.5);
  if (uv.x<0.0 || uv.x>1.0 || uv.y<0.0 || uv.y>1.0) discard;
  gl_FragColor = vec4(ray.xy, -ray.z, 1.0);
  //gl_FragColor = vec4(uv.x, uv.y, 0.0, 1.0);
  //gl_FragColor = texture2D(u_texture, uv);
  
}
  '''

scene.run(main, show_fps=True, frame_interval=0)





