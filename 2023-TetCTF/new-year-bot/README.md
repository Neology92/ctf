- flag is under FL4G variable
- use Content-Type: "application/x-www-form-urlencoded" header to make valid POST req
- use "debug" param to check flag length
- flag length is 24 chars
- possible to fetch only for indexes in range of the longest array (which is 5)

- tried to use different operators (\*, +, -, ()) in uncommon way
- unfortunately there's an restricton based on all numbers concatenation and 5> comparision (2\*3 --> 23 --> 23 < 5 --> False )
- thought about "eval" exploiting, but impossible to pass any letter. Injection is less likely.
