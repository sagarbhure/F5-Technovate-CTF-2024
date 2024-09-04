package main

import (
	// "html/template"
	"fmt"
	"log"
	"net/http"
)

func main() {
    // Serve static files from the "static" directory
    fs := http.FileServer(http.Dir("./static"))
    http.Handle("/static/", http.StripPrefix("/static/", fs))
    

    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintln(w, "Welcome to the Go Web App!")
    })

    // Hidden route
    http.HandleFunc("/secret", func(w http.ResponseWriter, r *http.Request) {
        if r.Method == http.MethodGet {
            fmt.Fprintln(w, "Here is the sensitive data:[ .... .. -.. -.. . -. ..--.- --. --- ..--.- .-. --- ..- - . ]")
        } else {
            http.NotFound(w, r)
        }
    })

    log.Println("Server started on :9994")
    log.Fatal(http.ListenAndServe(":9994", nil))
}
