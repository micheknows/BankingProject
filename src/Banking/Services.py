from HelperFunctions import HelperFunctions
from Service import Service, Loan, CreditCard
from Data import Data
from operator import attrgetter


class Services:

    def __init__(self):
        self.services = Data.retrieve_data("services")

    def apply_service(self, service_type, amt, customer_id, customers, purpose):
        if service_type == "loan":
            self.services.append(Loan(HelperFunctions.get_next_id([service.service_id for service in self.services]), customer_id, amt, customers, purpose))
        else:
            self.services.append(CreditCard(HelperFunctions.get_next_id([service.service_id for service in self.services]), customer_id, amt, customers))
        Data.save_data(self.services, "services")
        print(str(self.services[len(self.services)-1]))

    def view_services_list(self, customer_id):
        view_list = [service for service in self.services if service.customer_id==customer_id and not service.denied]
        view_list.sort(key=attrgetter('approved'), reverse=True)
        deny_list = [service for service in self.services if service.customer_id==customer_id and service.denied]
        if len(view_list) > 0 or len(deny_list) > 0:
            for service in view_list:
                print(str(service))
            for service in deny_list:
                print(str(service))
        else:
            print("No active services for customer.")

