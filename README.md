# Fucks as a Service by the Institute for Unnecessary Technology

- [FaaS Homepage](https://faas.unnecessary.tech/)
- [Github](https://github.com/devries/faas)
- [API Documentation](https://faas.unnecessary.tech/api/)

## Introduction

We at the Institute for Unnecessary Technology are pleased to announce our
newest product, Fucks as a Service, but before we delve into that we'd like to
speak a bit about our company and our vision. 

As chief scientist of the Institute, I, Christopher De Vries, am charged with
making products which do not enrich your life, but instead accompany you in
your march toward your inevitable death. Items such as our dad joke server,
our defunct blog, and our line of unscented perfumes are not such much runaway
hits as they are things you will have trouble finding through Google. Think of
us as a less successful Sharper Image for the new millennium. Well all that is
about to stay remarkably the same, with the introduction of Fucks as a
Service.

2017 has been a tough year, and we've had to give a lot of fucks. These fucks
can best be described in the medium of memes.

* We've had the inauguration of Donald Trump.<br/> ![How the fuck did this guy win?](static/piccard_win.jpg)
* The attempt to eliminate the Affordable Care Act.<br/>
  ![Get the fuck off my Obamacare](static/rent_obamacare.jpg)
* The revelation that most men you admire probably tried to assault a woman or
  a child at some point.<br/> 
  ![What the fuck is wrong with men?](static/herbert_men.jpg)
* And the new tax plan, which leaves middle-class taxes essentially
  unchanged.<br/>
  ![Where the fuck is that tax cut you promised?](static/trump_tax.jpg)

This has left most of us dangerously depleted when it comes to fucks.

![I've got no fucks to give](static/dog_fucks.jpg)

This seems like a problem which can be solved through the use of unnecessary
cloud technology, which is why we have introduced Fucks as a Service. Fucks as
a service provides fucks from an almost inexhaustible supply of fucks in the
cloud. You just ask for the number of fucks you need, and they are provided
through our user-friendly API. 

## Jumping In

The API fully documented using the recent [OpenAPI 3.0
Specification](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md),
so you know there is very little tooling available to produce client software.
The [openapi.yaml](https://github.com/devries/faas/blob/master/openapi.yaml)
on github documents the API, although we do our primary development in the
[bitbucket repository](https://bitbucket.org/devries/faas). The easiest way to
explor the API, and get a few demo fucks, is using the
[api explorer](https://faas.unnecessary.tech/api/).

To get some fucks, just perform a GET request to
`https://faas.unnecessary.tech/v1/get/{num}/fucks` where `{num}` should be
replaced with the number of fucks you want. For example to get 2 fucks, you
would make a GET request to `https://faas.unnecessary.tech/v1/get/2/fucks`.
The command below makes such a request using the [HTTPie](https://httpie.org/)
lbrary to make the request, [python](https://www.python.org/) to format the
response, and [Pygments](http://pygments.org/) to colorize the results.

```bash
http https://faas.unnecessary.tech/v1/give/2/fucks Accept:application/json | python -m json.tool | pygmentize -l json
```

The above command will return the JSON result below.

```json
{
    "fucks": [
        "fuck",
        "fuck"
    ],
    "status": "ok"
}
```

As you can see, the server has gathered and returned the two fucks you
requested from the cloud, and you now can give those fucks as need be. 

What about errors? Well, the fucks as a service server is full of helpful
error messages, for example if you try to query the wrong URL, as shown below,
you get a helpful error message.

```json
$ http https://faas.unnecessary.tech/v1/give/2/farts Accept:application/json | python -m json.tool | pygmentize -l json

{
    "message": "What the fucking fuck are you looking for?",
    "status": "error"
}
```

If you ask for `foo` fucks as shown below, you also get a helpful error
message.

```json
$ http https://faas.unnecessary.tech/v1/give/foo/fucks Accept:application/json | python -m json.tool | pygmentize -l json

{
    "message": "What the fuck kind of number is foo?",
    "status": "error"
}
```

Now, I know what you're thinking. JSON is fine, but for my enterprise level
fucks, I need to take advantage of XML. Well of course, just indicate that you
accept application/xml in the HTTP Accept header, and we'll give you
rock-solid enterprise-grade XML fucks.

```xml
$ http https://faas.unnecessary.tech/v1/give/2/fucks Accept:application/xml | xmllint --format - | pygmentize -l xml

<?xml version="1.0" encoding="UTF-8"?>
<ListOfFucks xmlns="http://faas.unnecessary.tech/schema">
  <status>ok</status>
  <fucks>
    <item>fuck</item>
    <item>fuck</item>
  </fucks>
  <observation>Why the fuck are you still using XML?</observation>
</ListOfFucks>
```

It also helpfully makes the observation, "Why the fuck are you still using
XML?"

## Conclusion

At the Institute for Unnecessary Technology we are happy we can fill this
critically unnecessary need for a cloud-based fucks service. Please note that
until we complete our first round of venture funding, there may be occasional
shortage of fucks as we gather more from the clouds. As a result there may be
occasional quotas.
