import { type RouteConfig, index, route } from "@react-router/dev/routes";

export default [
    index("routes/home.tsx"),
    route("client/:clientId", "routes/client_detail.tsx"),
] satisfies RouteConfig;
