package main

import (
	"fmt"
	"strings"
)

func main() {
	user := "Amboy nak makan"
	userName := strings.Fields(user)
	fmt.Printf("%v", userName)
}
