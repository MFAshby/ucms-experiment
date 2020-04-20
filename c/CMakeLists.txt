cmake_minimum_required(VERSION 3.16)

project(ucms-c)

add_executable(ucms main.c)
target_link_libraries(ucms microhttpd)
