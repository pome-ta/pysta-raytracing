precision highp float;

uniform float u_time;
uniform vec2 u_sprite_size;
//uniform float u_scale;
uniform sampler2D u_texture;
//uniform vec4 u_tint_color;
//uniform vec4 u_fill_color;
varying vec2 v_tex_coord;


// https://qiita.com/doxas/items/477fda867da467116f8d
// とりあえず陰影つけてみっか！！！！

struct Ray {
  vec3 origin;  // 視点
  vec3 direction;  // 方向
};

struct Sphere {
  float radius;  // 半径
  vec3 position;  // 位置
  vec3 color;  // 色
};

struct Intersection {
  bool hit;  // 交差したかどうかのフラグ
  vec3 hitPoint;  // 交点の座標
  vec3 normal;  // 交点位置の法線
  vec3 color;  // 交点位置の色
};

Intersection intersectSphere(Ray R, Sphere S) {
  Intersection i;
  vec3 a = R.origin - S.position;
  float b = dot(a, R.direction);
  float c = dot(a, a) - (S.radius * S.radius);
  float d = b * b - c;
  if(d > 0.0) {
    float t = -b - sqrt(d);
    if (t > 0.0) {
      i.hit = true;
      i.hitPoint = R.origin + R.direction * t;
      i.normal = normalize(i.hitPoint - S.position);
      float d = clamp(dot(normalize(vec3(1.0)), i.normal), 0.1, 1.0);
      i.color = S.color * d;
      return i;
    }
  }
  i.hit = false;
  i.hitPoint = vec3(0.0);
  i.normal = vec3(0.0);
  i.color = vec3(0.0);
  return i;
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
  Intersection i = intersectSphere(ray, sphere);
  
  
  gl_FragColor = vec4(i.color, 1.0);
}
