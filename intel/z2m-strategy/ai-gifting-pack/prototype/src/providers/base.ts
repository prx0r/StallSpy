import { Quote } from "../types";

export interface FulfillmentOrder {
  externalOrderId: string;
  sku: string;
  quantity: number;
  printFileUrl: string;
  recipient: {
    name: string;
    address1: string;
    address2?: string;
    city: string;
    postalCode: string;
    countryCode: string;
  };
}

export interface FulfillmentProvider {
  name: string;
  quote(input: FulfillmentOrder): Promise<Quote>;
  submit(input: FulfillmentOrder): Promise<{ providerOrderId: string }>;
  cancel(providerOrderId: string): Promise<boolean>;
}
