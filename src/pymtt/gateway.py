from py4j.java_gateway import (
    JavaGateway,
    GatewayParameters,
    JavaObject,
    JavaPackage,
    JVMView
)

class MttGateway(object):
    def __init__(self,port:int=25333):
        self.__gateway=JavaGateway(
            gateway_parameters=GatewayParameters(port=port)
        )

    def get_mechtatel(self)->JavaObject:
        return self.__gateway.entry_point
    
    def get_jvm(self)->JVMView:
        return self.__gateway.jvm
    
    def get_joml_package(self)->JavaPackage:
        return self.__gateway.jvm.org.joml
    
    def get_mechtatel_core_package(self)->JavaPackage:
        return self.__gateway.jvm.com.github.maeda6uiui.mechtatel.core
