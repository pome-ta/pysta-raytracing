precision highp float;

uniform float u_time;
uniform vec2 u_sprite_size;
//uniform float u_scale;
uniform sampler2D u_texture;
//uniform vec4 u_tint_color;
//uniform vec4 u_fill_color;
varying vec2 v_tex_coord;


// https://qiita.com/doxas/items/477fda867da467116f8d
// とりあえず球出してみっか！！！

struct Ray {
  vec3 origin;  // 視点
  vec3 direction;  // 方向
};

struct Sphere {
  float radius;  // 半径
  vec3 position;  // 位置
  vec3 color;  // 色
};

bool intersectSphere(Ray R, Sphere S) {
  vec3 a = R.origin - S.position;
  float b = dot(a, R.direction);
  float c = dot(a, a) - (S.radius * S.radius);
  float d = b * b - c;
  if(d > 0.0) {
    float t = -b - sqrt(d);
    return (t > 0.0);
  }
  return false;
}


void main(void) {
  // float t = u_time;
  // fragment position
  vec2 p = (v_tex_coord- vec2(0.5)) *2.0;
  
  // ray init
  Ray ray;
  ray.origin = vec3(0.0, 0.0, 5.0);
  ray.direction = normalize(vec3(p.x, p.y, -1.0));
  
  // sphere init
  Sphere sphere;
  sphere.radius = 1.0;
  sphere.position = vec3(0.0);
  sphere.color = vec3(1.0);
  
  // hit check
  vec3 destColor = vec3(0.0);
  if(intersectSphere(ray, sphere)) {
    destColor = sphere.color;
  }
  
  
  
  gl_FragColor = vec4(destColor, 1.0);
}
