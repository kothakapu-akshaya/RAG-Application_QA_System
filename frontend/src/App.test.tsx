import { render, screen } from "@testing-library/react";
import { test, expect } from "vitest";
import App from "./App";

test("renders Document Q&A heading", () => {
  render(<App />);
  expect(screen.getByText("Document Q&A")).toBeInTheDocument();
});