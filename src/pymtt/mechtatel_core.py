from py4j.java_gateway import(
    JavaPackage,
    JavaObject,
    JavaClass
)

class MechtatelCore(object):
    def __init__(self,mechtatel_core_package:JavaPackage,mechtatel:JavaObject):
        self.__core=mechtatel_core_package
        self.__mechtatel=mechtatel

        self.__animation=mechtatel_core_package.animation
        self.__camera=mechtatel_core_package.camera
        self.__nabor=mechtatel_core_package.nabor
        self.__sound=mechtatel_core_package.sound

    def draw_path(self)->JavaClass:
        return self.__core.DrawPath(self.__mechtatel)
    
    def screen_creator(self,screen_name:str)->JavaClass:
        return self.__core.ScreenCreator(self.__mechtatel,screen_name)
    
    def skybox_texture_creator(
            self,
            screen_name:str,
            texture_dirname:str,
            texture_extension:str,
            generate_mipmaps:bool)->JavaClass:
        return self.__core.SkyboxTextureCreator(
            self.__mechtatel,
            screen_name,
            texture_dirname,
            texture_extension,
            generate_mipmaps
        )
    
    def animation_info(self,json_filepath:str)->JavaClass:
        return self.__animation.AnimationInfo(json_filepath)
    
    def free_camera(self,camera:JavaClass)->JavaClass:
        return self.__camera.FreeCamera(camera)
    
    def flexible_nabor_info(self,vert_shader_filepath:str,frag_shader_filepath:str)->JavaClass:
        return self.__nabor.FlexibleNaborInfo(vert_shader_filepath,frag_shader_filepath)
    
    def sound_2d(self,sound_filepath:str)->JavaClass:
        return self.__sound.Sound2D(sound_filepath)
    
    def sound_3d(self,sound_filepath:str,loop:bool,relative:bool)->JavaClass:
        return self.__sound.Sound3D(sound_filepath,loop,relative)
    
    def duplicate_sound_3d(self,sound:JavaClass,loop:bool,relative:bool)->JavaClass:
        return self.__sound.Sound3D(sound,loop,relative)
    
    def close_window(self):
        self.__mechtatel.closeWindow()

    def get_window_width(self)->int:
        return self.__mechtatel.getWindowWidth()
    
    def get_window_height(self)->int:
        return self.__mechtatel.getWindowHeight()
    
    def get_fps(self)->int:
        return self.__mechtatel.getFPS()
    
    def get_seconds_per_frame(self)->float:
        return self.__mechtatel.getSecondsPerFrame()
    
    def get_keyboard_pressing_count(self,key:str)->int:
        return self.__mechtatel.getKeyboardPressingCount(key)
    
    def get_keyboard_releasing_count(self,key:str)->int:
        return self.__mechtatel.getKeyboardReleasingCount(key)
    
    def get_mouse_pressing_count(self,key:str)->int:
        return self.__mechtatel.getMousePressingCount(key)
    
    def get_mouse_releasing_count(self,key:str)->int:
        return self.__mechtatel.getMouseReleasingCount(key)
    
    def get_cursor_pos_x(self)->int:
        return self.__mechtatel.getCursorPosX()
    
    def get_cursor_pos_y(self)->int:
        return self.__mechtatel.getCursorPosY()
    
    def set_cursor_pos(self,x:int,y:int):
        self.__mechtatel.setCursorPos(x,y)
    
    def fix_cursor(self):
        self.__mechtatel.fixCursor()

    def unfix_cursor(self):
        self.__mechtatel.unfixCursor()

    def set_cursor_mode(self,cursor_mode:str):
        self.__mechtatel.setCursorMode(cursor_mode)

    def sort_components(self):
        self.__mechtatel.sortComponents()

    def create_model3d(self,screen_name:str,model_filepath:str)->JavaClass:
        return self.__mechtatel.createModel3D(screen_name,model_filepath)
    
    def duplicate_model3d(self,src_model:JavaClass)->JavaClass:
        return self.__mechtatel.duplicateModel3D(src_model)
