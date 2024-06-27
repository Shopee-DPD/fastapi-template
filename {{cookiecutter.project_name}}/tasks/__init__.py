from invoke import Collection

from tasks import env, secure, style, test

namespace = Collection()
namespace.add_collection(env)
namespace.add_collection(secure)
namespace.add_collection(style)
namespace.add_collection(test)
