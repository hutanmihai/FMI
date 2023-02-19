cmake_minimum_required(VERSION 3.22)
project(lab9)

set(CMAKE_CXX_STANDARD 14)

set(UTIL_SOURCE_FILES util/IoBase.h util/IoBase.cpp util/functions.h util/functions.cpp)
#add_executable(lab9 ex0.cpp ${UTIL_SOURCE_FILES})
#add_executable(lab9 ex1.cpp ${UTIL_SOURCE_FILES})
#add_executable(lab9 ex2.cpp ${UTIL_SOURCE_FILES})
#add_executable(lab9 ex3.cpp ${UTIL_SOURCE_FILES})
add_executable(lab9 simulare_colocviu.cpp ${UTIL_SOURCE_FILES})
