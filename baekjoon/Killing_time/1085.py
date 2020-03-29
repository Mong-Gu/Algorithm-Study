x, y, w, h = map(int, input().split())
print(min(min(w-x, w-(w-x)), min(h-y, h-(h-y))))