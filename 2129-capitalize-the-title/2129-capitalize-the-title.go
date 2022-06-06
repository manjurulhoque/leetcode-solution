func capitalizeTitle(title string) string {
    words := strings.Split(title, " ")
    var new_title []string
    // fmt.Println(words)
    for i := 0; i < len(words); i++ {
        if len(words[i]) > 2 {
            new_title = append(new_title, strings.Title(strings.ToLower(words[i])))
        } else {
            new_title = append(new_title, strings.ToLower(words[i]))
        }
    }
    return strings.Join(new_title, " ")
}