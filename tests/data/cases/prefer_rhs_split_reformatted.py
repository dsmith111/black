# Test cases separate from `prefer_rhs_split.py` that contains unformatted source.

# Left hand side fits in a single line but will still be exploded by the
# magic trailing comma.
first_value, (m1, m2,), third_value = xxxxxx_yyyyyy_zzzzzz_wwwwww_uuuuuuu_vvvvvvvvvvv(
    arg1,
    arg2,
)

# Make when when the left side of assignment plus the opening paren "... = (" is
# exactly line length limit + 1, it won't be split like that.
xxxxxxxxx_yyy_zzzzzzzz[xx.xxxxxx(x_yyy_zzzzzz.xxxxx[0]), x_yyy_zzzzzz.xxxxxx(xxxx=1)] = 1

# Regression test for #1187
print(
    dict(
        a=1,
        b=2 if some_kind_of_data is not None else some_other_kind_of_data,  # some explanation of why this is actually necessary
        c=3,
    )
)

# output


# Test cases separate from `prefer_rhs_split.py` that contains unformatted source.

# Left hand side fits in a single line but will still be exploded by the
# magic trailing comma.
(
    first_value,
    (
        m1,
        m2,
    ),
    third_value,
) = xxxxxx_yyyyyy_zzzzzz_wwwwww_uuuuuuu_vvvvvvvvvvv(
    arg1,
    arg2,
)

# Make when when the left side of assignment plus the opening paren "... = (" is
# exactly line length limit + 1, it won't be split like that.
xxxxxxxxx_yyy_zzzzzzzz[
    xx.xxxxxx(x_yyy_zzzzzz.xxxxx[0]), x_yyy_zzzzzz.xxxxxx(xxxx=1)
] = 1

# Regression test for #1187
print(
    dict(
        a=1,
        b=(
            2 if some_kind_of_data is not None else some_other_kind_of_data
        ),  # some explanation of why this is actually necessary
        c=3,
    )
)
                                                                                                                                                                                                                                                                                                                                                                                                                                            