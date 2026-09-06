import { FulfillmentOrder, FulfillmentProvider } from "./base";
import { Quote } from "../types";

export class GelatoProvider implements FulfillmentProvider {
  name = "gelato";

  constructor(private apiKey: string) {}

  async quote(input: FulfillmentOrder): Promise<Quote> {
    throw new Error("Gelato quote adapter not wired yet");
  }

  async submit(input: FulfillmentOrder): Promise<{ providerOrderId: string }> {
    throw new Error("Gelato order adapter not wired yet");
  }

  async cancel(providerOrderId: string): Promise<boolean> {
    throw new Error("Gelato cancel adapter not wired yet");
  }
}
