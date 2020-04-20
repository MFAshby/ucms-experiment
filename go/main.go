package main

import (
	"log"
	"net/http"
)

func main() {
	// Templates folder
	// Content folder 
	http.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("static"))))
	log.Fatal(http.ListenAndServe(":8080", nil))
}
