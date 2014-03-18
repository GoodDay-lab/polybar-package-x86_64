from utils import \
        get_namespace, \
        get_ext_name, \
        _n_item, \
        _ext

class ExtensionClass(object):
    def __init__(self, namespace):
        self.namespace = namespace

    def make_class(self):
        # if not self.namespace.is_ext:
        #     return ""
        # else:
        ns = get_namespace(self.namespace)
        if self.namespace.is_ext:
            base = "\n  : public xpp::generic::extension<extension, &xcb_%s_id>\n" % ns
            ctor = "    using base = xpp::generic::extension<extension, &xcb_%s_id>;\n" % ns + \
                   "    using base::base;\n"
        else:
            base = " "
            ctor = ""

        return \
'''\
template<typename Connection>
class protocol;

namespace event { template<typename Connection> class dispatcher; };
namespace error { class dispatcher; };

class extension%s{
  public:
%s\
    template<typename Connection>
    using protocol = xpp::%s::protocol<Connection>;
    template<typename Connection>
    using event_dispatcher = xpp::%s::event::dispatcher<Connection>;
    using error_dispatcher = xpp::%s::error::dispatcher;
};\
''' % (base,
       ctor,
       ns, # typedef xpp::protocol::%s protocol;
       ns, # typedef xpp::event::dispatcher::%s dispatcher;
       ns) # typedef xpp::error::dispatcher::%s dispatcher;
