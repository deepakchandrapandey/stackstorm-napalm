from lib.action import NapalmBaseAction


class NapalmPing(NapalmBaseAction):
    """Run a ping from a network device via NAPALM
    """

    def run(self, destination, source, ttl=255, pingtout=2, size=100, count=5, **std_kwargs):

        with self.get_driver(**std_kwargs) as device:

            result = {'raw': device.ping(destination, source, ttl, pingtout, size, count)}

            if self.htmlout:
                result['html'] = self.html_out(result['raw'])

        return (True, result)
