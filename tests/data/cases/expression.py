...
'some_string'
b'\\xa3'
Name
None
True
False
1
1.0
1j
True or False
True or False or None
True and False
True and False and None
(Name1 and Name2) or Name3
Name1 and Name2 or Name3
Name1 or (Name2 and Name3)
Name1 or Name2 and Name3
(Name1 and Name2) or (Name3 and Name4)
Name1 and Name2 or Name3 and Name4
Name1 or (Name2 and Name3) or Name4
Name1 or Name2 and Name3 or Name4
v1 << 2
1 >> v2
1 % finished
1 + v2 - v3 * 4 ^ 5 ** v6 / 7 // 8
((1 + v2) - (v3 * 4)) ^ (((5 ** v6) / 7) // 8)
not great
~great
+value
-1
~int and not v1 ^ 123 + v2 | True
(~int) and (not ((v1 ^ (123 + v2)) | True))
+really ** -confusing ** ~operator ** -precedence
flags & ~ select.EPOLLIN and waiters.write_task is not None
lambda arg: None
lambda a=True: a
lambda a, b, c=True: a
lambda a, b, c=True, *, d=(1 << v2), e='str': a
lambda a, b, c=True, *vararg, d=(v1 << 2), e='str', **kwargs: a + b
manylambdas = lambda x=lambda y=lambda z=1: z: y(): x()
foo = (lambda port_id, ignore_missing: {"port1": port1_resource, "port2": port2_resource}[port_id])
1 if True else 2
str or None if True else str or bytes or None
(str or None) if True else (str or bytes or None)
str or None if (1 if True else 2) else str or bytes or None
(str or None) if (1 if True else 2) else (str or bytes or None)
((super_long_variable_name or None) if (1 if super_long_test_name else 2) else (str or bytes or None))
{'2.7': dead, '3.7': (long_live or die_hard)}
{'2.7': dead, '3.7': (long_live or die_hard), **{'3.6': verygood}}
{**a, **b, **c}
{'2.7', '3.6', '3.7', '3.8', '3.9', ('4.0' if gilectomy else '3.10')}
({'a': 'b'}, (True or False), (+value), 'string', b'bytes') or None
()
(1,)
(1, 2)
(1, 2, 3)
[]
[1, 2, 3, 4, 5, 6, 7, 8, 9, (10 or A), (11 or B), (12 or C)]
[1, 2, 3,]
[*a]
[*range(10)]
[*a, 4, 5,]
[4, *a, 5,]
[this_is_a_very_long_variable_which_will_force_a_delimiter_split, element, another, *more]
{i for i in (1, 2, 3)}
{(i ** 2) for i in (1, 2, 3)}
{(i ** 2) for i, _ in ((1, 'a'), (2, 'b'), (3, 'c'))}
{((i ** 2) + j) for i in (1, 2, 3) for j in (1, 2, 3)}
[i for i in (1, 2, 3)]
[(i ** 2) for i in (1, 2, 3)]
[(i ** 2) for i, _ in ((1, 'a'), (2, 'b'), (3, 'c'))]
[((i ** 2) + j) for i in (1, 2, 3) for j in (1, 2, 3)]
{i: 0 for i in (1, 2, 3)}
{i: j for i, j in ((1, 'a'), (2, 'b'), (3, 'c'))}
{a: b * 2 for a, b in dictionary.items()}
{a: b * -2 for a, b in dictionary.items()}
{k: v for k, v in this_is_a_very_long_variable_which_will_cause_a_trailing_comma_which_breaks_the_comprehension}
Python3 > Python2 > COBOL
Life is Life
call()
call(arg)
call(kwarg='hey')
call(arg, kwarg='hey')
call(arg, another, kwarg='hey', **kwargs)
call(this_is_a_very_long_variable_which_will_force_a_delimiter_split, arg, another, kwarg='hey', **kwargs)  # note: no trailing comma pre-3.6
call(*gidgets[:2])
call(a, *gidgets[:2])
call(**self.screen_kwargs)
call(b, **self.screen_kwargs)
lukasz.langa.pl
call.me(maybe)
1 .real
1.0 .real
....__class__
list[str]
dict[str, int]
tuple[str, ...]
tuple[
    str, int, float, dict[str, int]
]
tuple[str, int, float, dict[str, int],]
very_long_variable_name_filters: t.List[
    t.Tuple[str, t.Union[str, t.List[t.Optional[str]]]],
]
xxxx_xxxxx_xxxx_xxx: Callable[..., List[SomeClass]] = classmethod(  # type: ignore
    sync(async_xxxx_xxx_xxxx_xxxxx_xxxx_xxx.__func__)
)
xxxx_xxx_xxxx_xxxxx_xxxx_xxx: Callable[..., List[SomeClass]] = classmethod(  # type: ignore
    sync(async_xxxx_xxx_xxxx_xxxxx_xxxx_xxx.__func__)
)
xxxx_xxx_xxxx_xxxxx_xxxx_xxx: Callable[
    ..., List[SomeClass]
] = classmethod(sync(async_xxxx_xxx_xxxx_xxxxx_xxxx_xxx.__func__))  # type: ignore
slice[0]
slice[0:1]
slice[0:1:2]
slice[:]
slice[:-1]
slice[1:]
slice[::-1]
slice[d :: d + 1]
slice[:c, c - 1]
numpy[:, 0:1]
numpy[:, :-1]
numpy[0, :]
numpy[:, i]
numpy[0, :2]
numpy[:N, 0]
numpy[:2, :4]
numpy[2:4, 1:5]
numpy[4:, 2:]
numpy[:, (0, 1, 2, 5)]
numpy[0, [0]]
numpy[:, [i]]
numpy[1 : c + 1, c]
numpy[-(c + 1) :, d]
numpy[:, l[-2]]
numpy[:, ::-1]
numpy[np.newaxis, :]
(str or None) if (sys.version_info[0] > (3,)) else (str or bytes or None)
{'2.7': dead, '3.7': long_live or die_hard}
{'2.7', '3.6', '3.7', '3.8', '3.9', '4.0' if gilectomy else '3.10'}
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10 or A, 11 or B, 12 or C]
(SomeName)
SomeName
(Good, Bad, Ugly)
(i for i in (1, 2, 3))
((i ** 2) for i in (1, 2, 3))
((i ** 2) for i, _ in ((1, 'a'), (2, 'b'), (3, 'c')))
(((i ** 2) + j) for i in (1, 2, 3) for j in (1, 2, 3))
(*starred,)
{"id": "1","type": "type","started_at": now(),"ended_at": now() + timedelta(days=10),"priority": 1,"import_session_id": 1,**kwargs}
a = (1,)
b = 1,
c = 1
d = (1,) + a + (2,)
e = (1,).count(1)
f = 1, *range(10)
g = 1, *"ten"
what_is_up_with_those_new_coord_names = (coord_names + set(vars_to_create)) + set(vars_to_remove)
what_is_up_with_those_new_coord_names = (coord_names | set(vars_to_create)) - set(vars_to_remove)
result = session.query(models.Customer.id).filter(models.Customer.account_id == account_id, models.Customer.email == email_address).order_by(models.Customer.id.asc()).all()
result = session.query(models.Customer.id).filter(models.Customer.account_id == account_id, models.Customer.email == email_address).order_by(models.Customer.id.asc(),).all()
Ø = set()
authors.łukasz.say_thanks()
mapping = {
    A: 0.25 * (10.0 / 12),
    B: 0.1 * (10.0 / 12),
    C: 0.1 * (10.0 / 12),
    D: 0.1 * (10.0 / 12),
}

def gen():
    yield from outside_of_generator
    a = (yield)
    b = ((yield))
    c = (((yield)))

async def f():
    await some.complicated[0].call(with_args=(True or (1 is not 1)))
print(* [] or [1])
print(**{1: 3} if False else {x: x for x in range(3)})
print(* lambda x: x)
assert(not Test),("Short message")
assert this is ComplexTest and not requirements.fit_in_a_single_line(force=False), "Short message"
assert(((parens is TooMany)))
for x, in (1,), (2,), (3,): ...
for y in (): ...
for z in (i for i in (1, 2, 3)): ...
for i in (call()): ...
for j in (1 + (2 + 3)): ...
while(this and that): ...
for addr_family, addr_type, addr_proto, addr_canonname, addr_sockaddr in socket.getaddrinfo('google.com', 'http'):
    pass
a = aaaa.bbbb.cccc.dddd.eeee.ffff.gggg.hhhh.iiii.jjjj.kkkk.llll.mmmm.nnnn.oooo.pppp in qqqq.rrrr.ssss.tttt.uuuu.vvvv.xxxx.yyyy.zzzz
a = aaaa.bbbb.cccc.dddd.eeee.ffff.gggg.hhhh.iiii.jjjj.kkkk.llll.mmmm.nnnn.oooo.pppp not in qqqq.rrrr.ssss.tttt.uuuu.vvvv.xxxx.yyyy.zzzz
a = aaaa.bbbb.cccc.dddd.eeee.ffff.gggg.hhhh.iiii.jjjj.kkkk.llll.mmmm.nnnn.oooo.pppp is qqqq.rrrr.ssss.tttt.uuuu.vvvv.xxxx.yyyy.zzzz
a = aaaa.bbbb.cccc.dddd.eeee.ffff.gggg.hhhh.iiii.jjjj.kkkk.llll.mmmm.nnnn.oooo.pppp is not qqqq.rrrr.ssss.tttt.uuuu.vvvv.xxxx.yyyy.zzzz
if (
    threading.current_thread() != threading.main_thread() and
    threading.current_thread() != threading.main_thread() or
    signal.getsignal(signal.SIGINT) != signal.default_int_handler
):
    return True
if (
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa |
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
):
    return True
if (
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa &
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
):
    return True
if (
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa +
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
):
    return True
if (
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa -
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
):
    return True
if (
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa *
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
):
    return True
if (
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa /
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
):
    return True
if (
    ~ aaaa.a + aaaa.b - aaaa.c * aaaa.d / aaaa.e | aaaa.f & aaaa.g % aaaa.h ^ aaaa.i << aaaa.k >> aaaa.l ** aaaa.m // aaaa.n
):
    return True
if (
    ~ aaaaaaaa.a + aaaaaaaa.b - aaaaaaaa.c @ aaaaaaaa.d / aaaaaaaa.e | aaaaaaaa.f & aaaaaaaa.g % aaaaaaaa.h ^ aaaaaaaa.i << aaaaaaaa.k >> aaaaaaaa.l ** aaaaaaaa.m // aaaaaaaa.n
):
    return True
if (
    ~ aaaaaaaaaaaaaaaa.a + aaaaaaaaaaaaaaaa.b - aaaaaaaaaaaaaaaa.c * aaaaaaaaaaaaaaaa.d @ aaaaaaaaaaaaaaaa.e | aaaaaaaaaaaaaaaa.f & aaaaaaaaaaaaaaaa.g % aaaaaaaaaaaaaaaa.h ^ aaaaaaaaaaaaaaaa.i << aaaaaaaaaaaaaaaa.k >> aaaaaaaaaaaaaaaa.l ** aaaaaaaaaaaaaaaa.m // aaaaaaaaaaaaaaaa.n
):
    return True
aaaaaaaaaaaaaaaa + aaaaaaaaaaaaaaaa - aaaaaaaaaaaaaaaa * (aaaaaaaaaaaaaaaa + aaaaaaaaaaaaaaaa) / (aaaaaaaaaaaaaaaa + aaaaaaaaaaaaaaaa + aaaaaaaaaaaaaaaa)
aaaaaaaaaaaaaaaa + aaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa >> aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa << aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
bbbb >> bbbb * bbbb
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ^bbbb.a & aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa^aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
last_call()
# standalone comment at ENDMARKER


# output


...
"some_string"
b"\\xa3"
Name
None
True
False
1
1.0
1j
True or False
True or False or None
True and False
True and False and None
(Name1 and Name2) or Name3
Name1 and Name2 or Name3
Name1 or (Name2 and Name3)
Name1 or Name2 and Name3
(Name1 and Name2) or (Name3 and Name4)
Name1 and Name2 or Name3 and Name4
Name1 or (Name2 and Name3) or Name4
Name1 or Name2 and Name3 or Name4
v1 << 2
1 >> v2
1 % finished
1 + v2 - v3 * 4 ^ 5**v6 / 7 // 8
((1 + v2) - (v3 * 4)) ^ (((5**v6) / 7) // 8)
not great
~great
+value
-1
~int and not v1 ^ 123 + v2 | True
(~int) and (not ((v1 ^ (123 + v2)) | True))
+(really ** -(confusing ** ~(operator**-precedence)))
flags & ~select.EPOLLIN and waiters.write_task is not None
lambda arg: None
lambda a=True: a
lambda a, b, c=True: a
lambda a, b, c=True, *, d=(1 << v2), e="str": a
lambda a, b, c=True, *vararg, d=(v1 << 2), e="str", **kwargs: a + b
manylambdas = lambda x=lambda y=lambda z=1: z: y(): x()
foo = lambda port_id, ignore_missing: {
    "port1": port1_resource,
    "port2": port2_resource,
}[port_id]
1 if True else 2
str or None if True else str or bytes or None
(str or None) if True else (str or bytes or None)
str or None if (1 if True else 2) else str or bytes or None
(str or None) if (1 if True else 2) else (str or bytes or None)
(
    (super_long_variable_name or None)
    if (1 if super_long_test_name else 2)
    else (str or bytes or None)
)
{"2.7": dead, "3.7": (long_live or die_hard)}
{"2.7": dead, "3.7": (long_live or die_hard), **{"3.6": verygood}}
{**a, **b, **c}
{"2.7", "3.6", "3.7", "3.8", "3.9", ("4.0" if gilectomy else "3.10")}
({"a": "b"}, (True or False), (+value), "string", b"bytes") or None
()
(1,)
(1, 2)
(1, 2, 3)
[]
[1, 2, 3, 4, 5, 6, 7, 8, 9, (10 or A), (11 or B), (12 or C)]
[
    1,
    2,
    3,
]
[*a]
[*range(10)]
[
    *a,
    4,
    5,
]
[
    4,
    *a,
    5,
]
[
    this_is_a_very_long_variable_which_will_force_a_delimiter_split,
    element,
    another,
    *more,
]
{i for i in (1, 2, 3)}
{(i**2) for i in (1, 2, 3)}
{(i**2) for i, _ in ((1, "a"), (2, "b"), (3, "c"))}
{((i**2) + j) for i in (1, 2, 3) for j in (1, 2, 3)}
[i for i in (1, 2, 3)]
[(i**2) for i in (1, 2, 3)]
[(i**2) for i, _ in ((1, "a"), (2, "b"), (3, "c"))]
[((i**2) + j) for i in (1, 2, 3) for j in (1, 2, 3)]
{i: 0 for i in (1, 2, 3)}
{i: j for i, j in ((1, "a"), (2, "b"), (3, "c"))}
{a: b * 2 for a, b in dictionary.items()}
{a: b * -2 for a, b in dictionary.items()}
{
    k: v
    for k, v in this_is_a_very_long_variable_which_will_cause_a_trailing_comma_which_breaks_the_comprehension
}
Python3 > Python2 > COBOL
Life is Life
call()
call(arg)
call(kwarg="hey")
call(arg, kwarg="hey")
call(arg, another, kwarg="hey", **kwargs)
call(
    this_is_a_very_long_variable_which_will_force_a_delimiter_split,
    arg,
    another,
    kwarg="hey",
    **kwargs
)  # note: no trailing comma pre-3.6
call(*gidgets[:2])
call(a, *gidgets[:2])
call(**self.screen_kwargs)
call(b, **self.screen_kwargs)
lukasz.langa.pl
call.me(maybe)
(1).real
(1.0).real
....__class__
list[str]
dict[str, int]
tuple[str, ...]
tuple[str, int, float, dict[str, int]]
tuple[
    str,
    int,
    float,
    dict[str, int],
]
very_long_variable_name_filters: t.List[
    t.Tuple[str, t.Union[str, t.List[t.Optional[str]]]],
]
xxxx_xxxxx_xxxx_xxx: Callable[..., List[SomeClass]] = classmethod(  # type: ignore
    sync(async_xxxx_xxx_xxxx_xxxxx_xxxx_xxx.__func__)
)
xxxx_xxx_xxxx_xxxxx_xxxx_xxx: Callable[..., List[SomeClass]] = classmethod(  # type: ignore
    sync(async_xxxx_xxx_xxxx_xxxxx_xxxx_xxx.__func__)
)
xxxx_xxx_xxxx_xxxxx_xxxx_xxx: Callable[..., List[SomeClass]] = classmethod(
    sync(async_xxxx_xxx_xxxx_xxxxx_xxxx_xxx.__func__)
)  # type: ignore
slice[0]
slice[0:1]
slice[0:1:2]
slice[:]
slice[:-1]
slice[1:]
slice[::-1]
slice[d :: d + 1]
slice[:c, c - 1]
numpy[:, 0:1]
numpy[:, :-1]
numpy[0, :]
numpy[:, i]
numpy[0, :2]
numpy[:N, 0]
numpy[:2, :4]
numpy[2:4, 1:5]
numpy[4:, 2:]
numpy[:, (0, 1, 2, 5)]
numpy[0, [0]]
numpy[:, [i]]
numpy[1 : c + 1, c]
numpy[-(c + 1) :, d]
numpy[:, l[-2]]
numpy[:, ::-1]
numpy[np.newaxis, :]
(str or None) if (sys.version_info[0] > (3,)) else (str or bytes or None)
{"2.7": dead, "3.7": long_live or die_hard}
{"2.7", "3.6", "3.7", "3.8", "3.9", "4.0" if gilectomy else "3.10"}
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10 or A, 11 or B, 12 or C]
(SomeName)
SomeName
(Good, Bad, Ugly)
(i for i in (1, 2, 3))
((i**2) for i in (1, 2, 3))
((i**2) for i, _ in ((1, "a"), (2, "b"), (3, "c")))
(((i**2) + j) for i in (1, 2, 3) for j in (1, 2, 3))
(*starred,)
{
    "id": "1",
    "type": "type",
    "started_at": now(),
    "ended_at": now() + timedelta(days=10),
    "priority": 1,
    "import_session_id": 1,
    **kwargs,
}
a = (1,)
b = (1,)
c = 1
d = (1,) + a + (2,)
e = (1,).count(1)
f = 1, *range(10)
g = 1, *"ten"
what_is_up_with_those_new_coord_names = (coord_names + set(vars_to_create)) + set(
    vars_to_remove
)
what_is_up_with_those_new_coord_names = (coord_names | set(vars_to_create)) - set(
    vars_to_remove
)
result = (
    session.query(models.Customer.id)
    .filter(
        models.Customer.account_id == account_id, models.Customer.email == email_address
    )
    .order_by(models.Customer.id.asc())
    .all()
)
result = (
    session.query(models.Customer.id)
    .filter(
        models.Customer.account_id == account_id, models.Customer.email == email_address
    )
    .order_by(
        models.Customer.id.asc(),
    )
    .all()
)
Ø = set()
authors.łukasz.say_thanks()
mapping = {
    A: 0.25 * (10.0 / 12),
    B: 0.1 * (10.0 / 12),
    C: 0.1 * (10.0 / 12),
    D: 0.1 * (10.0 / 12),
}


def gen():
    yield from outside_of_generator
    a = yield
    b = yield
    c = yield


async def f():
    await some.complicated[0].call(with_args=(True or (1 is not 1)))


print(*[] or [1])
print(**{1: 3} if False else {x: x for x in range(3)})
print(*lambda x: x)
assert not Test, "Short message"
assert this is ComplexTest and not requirements.fit_in_a_single_line(
    force=False
), "Short message"
assert parens is TooMany
for (x,) in (1,), (2,), (3,):
    ...
for y in ():
    ...
for z in (i for i in (1, 2, 3)):
    ...
for i in call():
    ...
for j in 1 + (2 + 3):
    ...
while this and that:
    ...
for (
    addr_family,
    addr_type,
    addr_proto,
    addr_canonname,
    addr_sockaddr,
) in socket.getaddrinfo("google.com", "http"):
    pass
a = (
    aaaa.bbbb.cccc.dddd.eeee.ffff.gggg.hhhh.iiii.jjjj.kkkk.llll.mmmm.nnnn.oooo.pppp
    in qqqq.rrrr.ssss.tttt.uuuu.vvvv.xxxx.yyyy.zzzz
)
a = (
    aaaa.bbbb.cccc.dddd.eeee.ffff.gggg.hhhh.iiii.jjjj.kkkk.llll.mmmm.nnnn.oooo.pppp
    not in qqqq.rrrr.ssss.tttt.uuuu.vvvv.xxxx.yyyy.zzzz
)
a = (
    aaaa.bbbb.cccc.dddd.eeee.ffff.gggg.hhhh.iiii.jjjj.kkkk.llll.mmmm.nnnn.oooo.pppp
    is qqqq.rrrr.ssss.tttt.uuuu.vvvv.xxxx.yyyy.zzzz
)
a = (
    aaaa.bbbb.cccc.dddd.eeee.ffff.gggg.hhhh.iiii.jjjj.kkkk.llll.mmmm.nnnn.oooo.pppp
    is not qqqq.rrrr.ssss.tttt.uuuu.vvvv.xxxx.yyyy.zzzz
)
if (
    threading.current_thread() != threading.main_thread()
    and threading.current_thread() != threading.main_thread()
    or signal.getsignal(signal.SIGINT) != signal.default_int_handler
):
    return True
if (
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    | aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
):
    return True
if (
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    & aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
):
    return True
if (
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    + aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
):
    return True
if (
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    - aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
):
    return True
if (
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    * aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
):
    return True
if (
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    / aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
):
    return True
if (
    ~aaaa.a + aaaa.b - aaaa.c * aaaa.d / aaaa.e
    | aaaa.f & aaaa.g % aaaa.h ^ aaaa.i << aaaa.k >> aaaa.l**aaaa.m // aaaa.n
):
    return True
if (
    ~aaaaaaaa.a + aaaaaaaa.b - aaaaaaaa.c @ aaaaaaaa.d / aaaaaaaa.e
    | aaaaaaaa.f & aaaaaaaa.g % aaaaaaaa.h
    ^ aaaaaaaa.i << aaaaaaaa.k >> aaaaaaaa.l**aaaaaaaa.m // aaaaaaaa.n
):
    return True
if (
    ~aaaaaaaaaaaaaaaa.a
    + aaaaaaaaaaaaaaaa.b
    - aaaaaaaaaaaaaaaa.c * aaaaaaaaaaaaaaaa.d @ aaaaaaaaaaaaaaaa.e
    | aaaaaaaaaaaaaaaa.f & aaaaaaaaaaaaaaaa.g % aaaaaaaaaaaaaaaa.h
    ^ aaaaaaaaaaaaaaaa.i
    << aaaaaaaaaaaaaaaa.k
    >> aaaaaaaaaaaaaaaa.l**aaaaaaaaaaaaaaaa.m // aaaaaaaaaaaaaaaa.n
):
    return True
(
    aaaaaaaaaaaaaaaa
    + aaaaaaaaaaaaaaaa
    - aaaaaaaaaaaaaaaa
    * (aaaaaaaaaaaaaaaa + aaaaaaaaaaaaaaaa)
    / (aaaaaaaaaaaaaaaa + aaaaaaaaaaaaaaaa + aaaaaaaaaaaaaaaa)
)
aaaaaaaaaaaaaaaa + aaaaaaaaaaaaaaaa
(
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    >> aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    << aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
)
bbbb >> bbbb * bbbb
(
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    ^ bbbb.a & aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    ^ aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
)
last_call()
# standalone comment at ENDMARKER
                                                                                                                                                                                                                                                                                                                                                                                                                                            