## Here it is tricky to compe up with the right key. The obvious choice would be to use IP but think why,

class DomainResolver:
    def __init__(self):
        self.domain_ip_map = {}
        self.domain_sub_map = {}

    def register_domain(self, ip, domain):
        if domain in self.domain_ip_map.keys():
            print("failed to register domain, domain is already registered to an ip")
            return
        self.domain_ip_map[domain] = ip

    def register_subdomain(self, domain, subdomain):
        if domain not in self.domain_sub_map.keys():
            self.domain_sub_map[domain] = set()
        self.domain_sub_map[domain].add(subdomain)
        
    def has_subdomain(self, ip, domain, subdomain):
        ip_validation = domain in self.domain_ip_map.keys() and self.domain_ip_map[domain] ==  ip
        subdomain_validation = domain in self.domain_sub_map.keys() and subdomain in self.domain_sub_map[domain]
        print(ip_validation, subdomain_validation)
        if ip_validation and subdomain_validation:
            print("True")
            return True
        print("False")
        return False
        
resolver = DomainResolver()
resolver.register_domain("192.168.1.1", "example.com")
resolver.register_domain("192.168.1.1", "example.org")
resolver.register_domain("192.168.1.2", "domain.com")
resolver.register_subdomain("example.com", "a")
resolver.register_subdomain("example.com", "b")
print(resolver.domain_sub_map)
resolver.has_subdomain("192.168.1.1", "example.com", "a")  # Returns True
resolver.has_subdomain("192.168.1.1", "example.com", "c")  # Returns False
resolver.has_subdomain("127.0.0.1", "example.com", "a")    # Returns False
resolver.has_subdomain("192.168.1.1", "example.org", "a")  # Returns False
resolver.has_subdomain("192.168.1.2", "example.com", "a")  # Returns False