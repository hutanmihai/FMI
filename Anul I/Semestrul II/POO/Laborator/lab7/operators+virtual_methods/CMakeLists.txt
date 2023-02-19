cmake_minimum_required(VERSION 3.21)
project(lab7)

set(CMAKE_CXX_STANDARD 14)

set(UTIL_SOURCE_FILES util/IoBase.h util/IoBase.cpp util/functions.h util/functions.cpp)
#add_executable(lab7 main1.cpp ${UTIL_SOURCE_FILES})
add_executable(main main2.cpp ${UTIL_SOURCE_FILES})
