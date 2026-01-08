import { MoreVertical, Users, Archive } from "lucide-react";
import { Link } from "react-router-dom";
import { motion } from "framer-motion";

import TeacherLayout from "../../components/layout/TeacherLayout";
import { ARCHIVED_CLASSES } from "../../mocks/classes";
import { Button } from "../../components/ui/button";
import { Card, CardContent, CardFooter } from "../../components/ui/card";

// Motion Variants
const containerVariants = {
    hidden: { opacity: 0 },
    show: {
        opacity: 1,
        transition: {
            staggerChildren: 0.1
        }
    }
};

const itemVariants = {
    hidden: { opacity: 0, y: 20 },
    show: { opacity: 1, y: 0 }
};

const ArchivedClassCard = ({ cl }) => (
    <motion.div variants={itemVariants}>
        <Card className="overflow-hidden hover:shadow-lg transition-shadow duration-300 h-full flex flex-col border-0 shadow-md opacity-90 hover:opacity-100">
            <div className={`h-24 ${cl.bgPattern} relative p-4 flex flex-col justify-between`}>
                <div className="flex justify-between items-start text-white">
                    <Link to={`/teacher/class/${cl.id}`} className="hover:underline">
                        <h3 className="text-xl font-bold leading-tight tracking-tight">{cl.name}</h3>
                    </Link>
                    <Button variant="ghost" size="icon" className="text-white hover:bg-black/20 hover:text-white h-8 w-8">
                        <MoreVertical className="w-5 h-5" />
                    </Button>
                </div>
                <div className="flex items-center justify-between">
                    <p className="text-blue-50 text-sm font-medium opacity-90">{cl.section}</p>
                    <div className="flex items-center gap-1 bg-black/20 px-2 py-1 rounded-md">
                        <Archive className="w-3 h-3" />
                        <span className="text-xs font-medium">Archived</span>
                    </div>
                </div>
            </div>

            <CardContent className="p-4 flex-1 flex flex-col gap-4 mt-2">
                <div className="flex items-center justify-between text-muted-foreground text-sm font-medium">
                    <div className="flex items-center gap-2">
                        <Users className="w-4 h-4 text-gray-400" />
                        <span>{cl.students} Students</span>
                    </div>
                    <span>{cl.assignments} Assignments</span>
                </div>

                <div className="mt-auto pt-3 border-t">
                    <p className="text-gray-500 text-sm italic">
                        This class has been archived and is read-only
                    </p>
                </div>
            </CardContent>

            <CardFooter className="px-4 py-3 bg-gray-50/50 border-t flex justify-end">
                <Button variant="link" className="text-indigo-600 font-semibold p-0 h-auto" asChild>
                    <Link to={`/teacher/class/${cl.id}`}>
                        VIEW CLASS
                    </Link>
                </Button>
            </CardFooter>
        </Card>
    </motion.div>
);

export default function ArchivedClasses() {
    return (
        <TeacherLayout>
            <motion.div
                className="flex items-center justify-between mb-8"
                initial={{ opacity: 0, y: -20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5 }}
            >
                <div>
                    <div className="flex items-center gap-3 mb-2">
                        <Archive className="w-8 h-8 text-gray-400" />
                        <h1 className="text-3xl font-bold text-gray-900 tracking-tight">Archived Classes</h1>
                    </div>
                    <p className="text-muted-foreground mt-1 text-lg">
                        {ARCHIVED_CLASSES.length === 0 
                            ? "No archived classes yet"
                            : `View and access your ${ARCHIVED_CLASSES.length} archived ${ARCHIVED_CLASSES.length === 1 ? 'class' : 'classes'}`
                        }
                    </p>
                </div>
            </motion.div>

            {ARCHIVED_CLASSES.length === 0 ? (
                <motion.div
                    className="flex flex-col items-center justify-center py-16 px-4"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ delay: 0.2 }}
                >
                    <div className="w-24 h-24 rounded-full bg-gray-100 flex items-center justify-center mb-4">
                        <Archive className="w-12 h-12 text-gray-400" />
                    </div>
                    <h3 className="text-xl font-semibold text-gray-900 mb-2">No Archived Classes</h3>
                    <p className="text-gray-500 text-center max-w-md">
                        Classes you archive will appear here. Archived classes are read-only and can be accessed for reference.
                    </p>
                </motion.div>
            ) : (
                <motion.div
                    className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"
                    variants={containerVariants}
                    initial="hidden"
                    animate="show"
                >
                    {ARCHIVED_CLASSES.map((cl) => (
                        <ArchivedClassCard key={cl.id} cl={cl} />
                    ))}
                </motion.div>
            )}
        </TeacherLayout>
    );
}
