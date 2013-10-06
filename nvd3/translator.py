#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Tag(object):
    """Tag class"""

    def __init__(self, content=None):
        self.content = content
        self.attrs = ' '.join(['%s="%s"' % (attr, value)
                               for attr, value in self.attrs])

    def __str__(self):
        return '<%s%s>\n    %s\n</%s>' % (self.name, self.attrs and ' ' + self.attrs or '', self.content, self.name)


class ScriptTag(Tag):
    name = 'script'
    attrs = (('type', 'text/javascript'),)


class AnonymousFunction(object):
    def __init__(self, arguments, content):
        self.arguments = arguments
        self.content = content

    def __str__(self):
        return 'function(%s) { %s }' % (self.arguments, self.content)


class Function(object):

    def __init__(self, name):
        self.name = name
        self.statements = []

    def __str__(self):
        operations = [self.name]
        operations.extend(str(statement) for statement in self.statements)
        return '%s' % ('.'.join(operations),)

    def __getattr__(self, attr):
        self.statements.append(attr)
        return self

    def __call__(self, args=None):
        if isinstance(args, (Function, AnonymousFunction, basestring)):
            self.statements[-1] = self.statements[-1] + '(%s)' % (args,)
        else:
            self.statements[-1] = self.statements[-1] + '()'
        return self


class Assignment(object):

    def __init__(self, key, value, scoped=True):
        self.key = key
        self.value = value
        self.scoped = scoped

    def __str__(self):
        return '%s%s = %s;' % (self.scoped and 'var ' or '', self.key, self.value)


if __name__ == '__main__':
    nv = Function('nv').addGraph(
        AnonymousFunction('', Assignment('chart',
            Function('nv').models.pieChart(
                ).x(
                    AnonymousFunction('d', 'return d.label;')
                ).y(
                    AnonymousFunction('d', 'return d.value;')
                ).showLabels('true')
            )
        )
    )
    print nv
