import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { assignmentService } from '../../services/assignmentService';
import { Button } from '../../components/ui/button';
import { toast } from 'sonner';

export default function AIAnalysisTasks() {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchTasks = async () => {
    try {
      const res = await assignmentService.getAIAnalysisTasks();
      setTasks(res.data || []);
    } catch (e) {
      if (e.response?.status === 403) toast.error('Admin only');
      else toast.error('Failed to load');
      setTasks([]);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchTasks();
    const id = setInterval(fetchTasks, 8000);
    return () => clearInterval(id);
  }, []);

  const handleCancel = async (assignmentId) => {
    try {
      await assignmentService.cancelAIAnalysis(assignmentId);
      toast.success('Cancelled');
      fetchTasks();
    } catch (e) {
      toast.error(e.response?.data?.message || 'Cancel failed');
    }
  };

  if (loading) return <div className="p-6">Loading…</div>;

  return (
    <div className="p-6 max-w-2xl">
      <div className="flex items-center gap-4 mb-4">
        <Link to="/teacher/dashboard" className="text-indigo-600 hover:underline">← Back</Link>
        <h1 className="text-xl font-semibold">Running AI analyses</h1>
      </div>
      {tasks.length === 0 ? (
        <p className="text-gray-500">No active AI analysis tasks.</p>
      ) : (
        <ul className="space-y-2 border rounded-lg divide-y">
          {tasks.map((t) => (
            <li key={t.task_id} className="p-3 flex items-center justify-between gap-2">
              <div className="min-w-0">
                <p className="font-medium truncate">{t.assignment_title}</p>
                <p className="text-sm text-gray-500">
                  {t.status} · Batch {t.completed_batches}/{t.total_batches || '?'}
                </p>
              </div>
              <div className="flex gap-2 shrink-0">
                <Link to={`/teacher/assignment/${t.assignment_id}`}>
                  <Button variant="outline" size="sm">Open</Button>
                </Link>
                <Button variant="destructive" size="sm" onClick={() => handleCancel(t.assignment_id)}>
                  Cancel
                </Button>
              </div>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
