from tasks import add

result = add.delay(4, 4)
print("Is tak ready: %s" % result.ready())

run_result = result.get(timeout=1)
print('task result:%s' % run_result)