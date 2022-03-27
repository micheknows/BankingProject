from HelperFunctions import HelperFunctions
from Service import Service, Loan, CreditCard
from Data import Data
from operator import attrgetter
import logging


class Services:
    """
    A class to handle tasks for Services

    ...

    Attributes
    -----------
    services    :   List(Service)
        list of all service objects

    Methods
    ---------
    apply_service(service_type, customer_id):
        creates a customer application for a service
    view_services_list(customer_id)
        prints a list of services for a particular customer id

    """
    @property
    def logger(self):
        return self._logger

    @logger.setter
    def logger(self, logger):
        self._logger = logger

    @property
    def services(self):
        return self._services

    @services.setter
    def services(self, services):
        self._services = services

    def __init__(self):
        """
        Constructs all the necessary attributes for the Services object

        Parameters
        -----------
        None


        """

        logging.basicConfig(filename="banking.log",
                            format='%(asctime)s %(message)s',
                            filemode='a')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.services = Data.retrieve_data("services")

    def apply_service(self, service_type, customer_id):
        """
        creates a customer application for a service

        Parameters
        -------------
        service_type    :   str
            type of service applying for (i.e.  loan, credit card)
        customer_id     :   int
            id of the customer

        Returns
        -------------
        None

        """
        customers = Data.retrieve_data("customers")
        amt = HelperFunctions.get_float("How much do you want to apply for?")
        if amt > 0:
            if service_type == "loan":
                purpose = HelperFunctions.get_string("What is the purpose of the loan?")
                self.services.append(
                    Loan(HelperFunctions.get_next_id([service.service_id for service in self.services]), customer_id,
                         amt, customers, purpose))
            else:
                service_id = CreditCard(HelperFunctions.get_next_id([service.service_id for service in self.services]))
                self.services.append(service_id, customer_id, amt, customers)
        Data.save_data(self.services, "services")
        print(str(self.services[len(self.services)-1]))

    def view_services_list(self, customer_id):
        """
        prints a list of services that are associated with a particular customer id

        Parameters
        -------------
        customer_id     :   int
            id of the customer

        Returns
        -------------
        None

        """
        view_list = [service for service in self.services if service.customer_id == customer_id and not service.denied]
        view_list.sort(key=attrgetter('approved'), reverse=True)
        deny_list = [service for service in self.services if service.customer_id == customer_id and service.denied]
        if len(view_list) > 0 or len(deny_list) > 0:
            for service in view_list:
                print(str(service))
            for service in deny_list:
                print(str(service))
        else:
            print("No active services for customer.")
