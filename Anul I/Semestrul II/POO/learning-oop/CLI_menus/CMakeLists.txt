cmake_minimum_required(VERSION 3.21)
project(lab8)

set(CMAKE_CXX_STANDARD 14)

set(UTIL_SOURCE_FILES util/IoBase.h util/IoBase.cpp util/functions.h util/functions.cpp)

#add_executable(lab8 ex1.cpp ${UTIL_SOURCE_FILES})
#add_executable(lab8 ex2.cpp ${UTIL_SOURCE_FILES})
#add_executable(lab8 ex4.cpp ${UTIL_SOURCE_FILES})
add_executable(lab8 ex5.cpp ${UTIL_SOURCE_FILES})