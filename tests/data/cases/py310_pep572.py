# flags: --minimum-version=3.10
x[a:=0]
x[a := 0]
x[a := 0, b := 1]
x[5, b := 0]
x[a:=0,b:=1]

# output
x[a := 0]
x[a := 0]
x[a := 0, b := 1]
x[5, b := 0]
x[a := 0, b := 1]
                                                                                                                                                                                                                                                                                                                                                                                                                                            