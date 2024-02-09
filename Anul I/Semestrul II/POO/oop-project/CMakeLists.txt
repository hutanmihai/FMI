cmake_minimum_required(VERSION 3.22)
project(Colocvii)

set(CMAKE_CXX_STANDARD 14)

set(UTIL_SOURCE_FILES util/IoBase.h util/IoBase.cpp util/functions.h util/functions.cpp)
set(HEADERE_UTILE_IO 143_Hutan_Mihai-Alexandru/IO_TEMPLATE_VAR.h 143_Hutan_Mihai-Alexandru/IO_TEMPLATE_VAR.cpp 143_Hutan_Mihai-Alexandru/IO_TEMPLATE_VECTORS.h 143_Hutan_Mihai-Alexandru/IO_TEMPLATE_VECTORS.cpp)

#add_executable(Colocvii colocviu2021.cpp ${UTIL_SOURCE_FILES})
#add_executable(Colocvii colocviu2020.cpp)
#add_executable(Colocvii colocviu2015.cpp)
#add_executable(Colocvii colocviu2020_restanta.cpp)
#add_executable(Colocvii colocviu2020_restanta_toamna.cpp)
add_executable(Colocvii PREGATIRE_EXAMEN.cpp)