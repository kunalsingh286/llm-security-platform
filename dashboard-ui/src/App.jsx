import { useEffect, useState } from "react";
import { getLogs } from "./api";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer
} from "recharts";

export default function App() {

  const [logs, setLogs] = useState([]);

  useEffect(() => {

    loadLogs();

    const interval = setInterval(loadLogs, 5000);

    return () => clearInterval(interval);

  }, []);

  const loadLogs = async () => {

    try {
      const res = await getLogs();
      setLogs(res.data);

    } catch (err) {
      console.error(err);
    }
  };

  const stats = logs.reduce((acc, l) => {

    acc[l.status] = (acc[l.status] || 0) + 1;
    return acc;

  }, {});

  const chartData = Object.keys(stats).map(k => ({
    name: k,
    value: stats[k]
  }));

  return (
    <div className="min-h-screen bg-gray-100 p-6">

      <h1 className="text-3xl font-bold mb-6">
        LLM Security Platform — Admin Dashboard
      </h1>

      {/* Stats */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">

        {Object.entries(stats).map(([k, v]) => (

          <div
            key={k}
            className="bg-white p-4 rounded-xl shadow"
          >
            <p className="text-gray-500">{k}</p>
            <p className="text-2xl font-bold">{v}</p>
          </div>

        ))}

      </div>

      {/* Chart */}
      <div className="bg-white p-4 rounded-xl shadow mb-8">

        <h2 className="text-xl font-semibold mb-4">
          Request Summary
        </h2>

        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={chartData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Line dataKey="value" />
          </LineChart>
        </ResponsiveContainer>

      </div>

      {/* Logs */}
      <div className="bg-white p-4 rounded-xl shadow">

        <h2 className="text-xl font-semibold mb-4">
          Recent Audit Logs
        </h2>

        <div className="overflow-x-auto">

          <table className="w-full border">

            <thead className="bg-gray-200">
              <tr>
                <th className="p-2 border">Time</th>
                <th className="p-2 border">Prompt</th>
                <th className="p-2 border">Status</th>
                <th className="p-2 border">Decision</th>
              </tr>
            </thead>

            <tbody>

              {logs.map(l => (

                <tr key={l.id}>

                  <td className="p-2 border text-sm">
                    {new Date(l.timestamp).toLocaleString()}
                  </td>

                  <td className="p-2 border text-sm truncate max-w-xs">
                    {l.prompt}
                  </td>

                  <td className="p-2 border font-bold">
                    {l.status}
                  </td>

                  <td className="p-2 border">
                    {l.decision}
                  </td>

                </tr>

              ))}

            </tbody>

          </table>

        </div>

      </div>

    </div>
  );
}
