from py4j.java_gateway import(
    JavaPackage,
    JavaClass
)

class JOML(object):
    def __init__(self,joml_package:JavaPackage):
        self.__joml=joml_package

    def vector2f(self,x:float,y:float)->JavaClass:
        return self.__joml.Vector2f(x,y)

    def vector3f(self,x:float,y:float,z:float)->JavaClass:
        return self.__joml.Vector3f(x,y,z)
    
    def vector4f(self,x:float,y:float,z:float,w:float)->JavaClass:
        return self.__joml.Vector4f(x,y,z,w)
    
    def matrix4f(self)->JavaClass:
        return self.__joml.Matrix4f()
