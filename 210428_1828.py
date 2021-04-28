precision highp float;

uniform float u_time;
uniform vec2 u_sprite_size;
//uniform float u_scale;
uniform sampler2D u_texture;
//uniform vec4 u_tint_color;
//uniform vec4 u_fill_color;
varying vec2 v_tex_coord;


struct Ray{
  vec3 origin;
  vec3 direction;
};


void main(void) {
  float t = u_time;
  vec2 p = (v_tex_coord- vec2(0.5)) *2.0;
  
  // ray init
  Ray ray;
  ray.origin = vec3(0.0, 0.0, 5.0);
  ray.direction = normalize(vec3(p.x, p.y, -1.0));
  gl_FragColor = vec4(ray.direction, 1.0);
}
