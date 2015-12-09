import sys
sys.path.append('/usr/local/lib/python2.7/dist-packages')
import web

urls = (
    '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        form = web.input(name = "User", greet = "Hello")
        greeting = "%s, %s" % (form.greet, form.name)

        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()
