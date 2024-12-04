package utils

import "strings"

func Capitalize(s string) string {
	if len(s) == 0 {
		return s // Return an empty string if input is empty
	}

	return strings.ToUpper(string(s[0])) + s[1:]
}
